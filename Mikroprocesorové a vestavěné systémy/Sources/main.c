/* Header file with all the essential definitions for a given type of MCU */
#include "MK60D10.h"


/* Macros for bit-level registers manipulation */
#define GPIO_PIN_MASK	0x1Fu
#define GPIO_PIN(x)		(((1)<<(x & GPIO_PIN_MASK)))

/* Mapping buttons */
#define BTN_RIGHT 0x400     // Port E, bit 10
#define BTN_DOWN 0x1000    // Port E, bit 12
#define BTN_LEFT 0x8000000 // Port E, bit 27
#define BTN_UP 0x4000000 // Port E, bit 26



#define CLEAR_ROWS 0x0

/* Directions of movement */
#define DOWN 0
#define UP 1
#define LEFT 2
#define RIGHT 3

#define SNAKE_LENGTH 7

struct snake_cell_position{
	int x;
	int y;
};

struct snake_cell_position snake[SNAKE_LENGTH];

int direction=0; //starting direction
int x_start=4;//starting x
int y_start=10;//starting y

/* Configuration of the necessary MCU peripherals */
void SystemConfig() {
	/* Turn on all port clocks */
	SIM->SCGC5 = SIM_SCGC5_PORTA_MASK | SIM_SCGC5_PORTE_MASK;

	/* Set corresponding PTA pins (column activators of 74HC154) for GPIO functionality */
	PORTA->PCR[8] = ( 0|PORT_PCR_MUX(0x01) );  // A0
	PORTA->PCR[10] = ( 0|PORT_PCR_MUX(0x01) ); // A1
	PORTA->PCR[6] = ( 0|PORT_PCR_MUX(0x01) );  // A2
	PORTA->PCR[11] = ( 0|PORT_PCR_MUX(0x01) ); // A3

	/* Set corresponding PTA pins (rows selectors of 74HC154) for GPIO functionality */
	PORTA->PCR[26] = ( 0|PORT_PCR_MUX(0x01) );  // R0
	PORTA->PCR[24] = ( 0|PORT_PCR_MUX(0x01) );  // R1
	PORTA->PCR[9] = ( 0|PORT_PCR_MUX(0x01) );   // R2
	PORTA->PCR[25] = ( 0|PORT_PCR_MUX(0x01) );  // R3
	PORTA->PCR[28] = ( 0|PORT_PCR_MUX(0x01) );  // R4
	PORTA->PCR[7] = ( 0|PORT_PCR_MUX(0x01) );   // R5
	PORTA->PCR[27] = ( 0|PORT_PCR_MUX(0x01) );  // R6
	PORTA->PCR[29] = ( 0|PORT_PCR_MUX(0x01) );  // R7

	/*PORTE->PCR[10] = PORT_PCR_MUX(0x01); // SW2
	PORTE->PCR[12] = PORT_PCR_MUX(0x01); // SW3
	PORTE->PCR[27] = PORT_PCR_MUX(0x01); // SW4
	PORTE->PCR[26] = PORT_PCR_MUX(0x01); // SW5*/
	PORTE->PCR[10] =  ( PORT_PCR_ISF(0x01) | PORT_PCR_IRQC(0x0A) | PORT_PCR_MUX(0x01) | PORT_PCR_PE(0x01) | PORT_PCR_PS(0x01));
	PORTE->PCR[12] =  ( PORT_PCR_ISF(0x01) | PORT_PCR_IRQC(0x0A) | PORT_PCR_MUX(0x01) | PORT_PCR_PE(0x01) | PORT_PCR_PS(0x01));
	PORTE->PCR[27] =  ( PORT_PCR_ISF(0x01) | PORT_PCR_IRQC(0x0A) | PORT_PCR_MUX(0x01) | PORT_PCR_PE(0x01) | PORT_PCR_PS(0x01));
	PORTE->PCR[26] =  ( PORT_PCR_ISF(0x01) | PORT_PCR_IRQC(0x0A) | PORT_PCR_MUX(0x01) | PORT_PCR_PE(0x01) | PORT_PCR_PS(0x01));


	/* Set corresponding PTE pins (output enable of 74HC154) for GPIO functionality */
	PORTE->PCR[28] = ( 0|PORT_PCR_MUX(0x01) ); // #EN


	/* Change corresponding PTA port pins as outputs */
	PTA->PDDR = GPIO_PDDR_PDD(0x3F000FC0);

	/* Change corresponding PTE port pins as outputs */
	PTE->PDDR = GPIO_PDDR_PDD(GPIO_PIN(28));

	NVIC_ClearPendingIRQ(PORTE_IRQn);
	NVIC_EnableIRQ(PORTE_IRQn);
}

/* Function initializes PIT clock  */
void PIT_init(void){
	SIM->SCGC6 |= SIM_SCGC6_PIT_MASK;
	PIT_MCR = 0x00; // enable clock
	PIT_TFLG0 |= PIT_TFLG_TIF_MASK; // clear interruption
	PIT_TCTRL0 = PIT_TCTRL_TIE_MASK; // enable interruption
	PIT_TCTRL0 |= PIT_TCTRL_TEN_MASK; // start clock
	PIT_LDVAL0 = 25000;
	NVIC_ClearPendingIRQ(PIT0_IRQn);
	NVIC_EnableIRQ(PIT0_IRQn);
	PTA->PDOR &= GPIO_PDOR_PDO(CLEAR_ROWS);

}

/* Variable delay loop */
void delay(int t1, int t2)
{
	int i, j;
	for(i=0; i<t1; i++) {
		for(j=0; j<t2; j++);
	}
}


/* Conversion of requested column number into the 4-to-16 decoder control.  */
void column_select(unsigned int col_num)
{
	unsigned i, result, col_sel[4];

	for (i =0; i<4; i++) {
		result = col_num / 2;	  // Whole-number division of the input number
		col_sel[i] = col_num % 2;
		col_num = result;

		switch(i) {

			// Selection signal A0
		    case 0:
				((col_sel[i]) == 0) ? (PTA->PDOR &= ~GPIO_PDOR_PDO( GPIO_PIN(8))) : (PTA->PDOR |= GPIO_PDOR_PDO( GPIO_PIN(8)));
				break;

			// Selection signal A1
			case 1:
				((col_sel[i]) == 0) ? (PTA->PDOR &= ~GPIO_PDOR_PDO( GPIO_PIN(10))) : (PTA->PDOR |= GPIO_PDOR_PDO( GPIO_PIN(10)));
				break;

			// Selection signal A2
			case 2:
				((col_sel[i]) == 0) ? (PTA->PDOR &= ~GPIO_PDOR_PDO( GPIO_PIN(6))) : (PTA->PDOR |= GPIO_PDOR_PDO( GPIO_PIN(6)));
				break;

			// Selection signal A3
			case 3:
				((col_sel[i]) == 0) ? (PTA->PDOR &= ~GPIO_PDOR_PDO( GPIO_PIN(11))) : (PTA->PDOR |= GPIO_PDOR_PDO( GPIO_PIN(11)));
				break;

			// Otherwise nothing to do...
			default:
				break;
		}
	}
}

/* Function selects row of the matrix display */
void row_select(int row){
	switch(row){
			case 0:
	            PTA->PDOR |= GPIO_PDOR_PDO( GPIO_PIN(29));
				break;
			case 1:
	            PTA->PDOR |= GPIO_PDOR_PDO( GPIO_PIN(27));
				break;
			case 2:
	            PTA->PDOR |= GPIO_PDOR_PDO( GPIO_PIN(7));
				break;
			case 3:
	            PTA->PDOR |= GPIO_PDOR_PDO( GPIO_PIN(28));
				break;
			case 4:
	            PTA->PDOR |= GPIO_PDOR_PDO( GPIO_PIN(25));
				break;
			case 5:
	            PTA->PDOR |= GPIO_PDOR_PDO( GPIO_PIN(9));
				break;
			case 6:
	            PTA->PDOR |= GPIO_PDOR_PDO( GPIO_PIN(24));
				break;
			case 7:
	            PTA->PDOR |= GPIO_PDOR_PDO( GPIO_PIN(26));
				break;
	}
}

/* Function handles interruptions from buttons and sets direction of the snake */
void PORTE_IRQHandler(void){
	if ((PORTE->ISFR & BTN_UP)&&(direction != DOWN)){
		direction=UP;
	}
	else if ((PORTE->ISFR & BTN_DOWN)&&(direction != UP)){
		direction=DOWN;
	}
	else if ((PORTE->ISFR & BTN_LEFT)&&(direction != RIGHT)){
		direction=LEFT;
	}
	else if ((PORTE->ISFR & BTN_RIGHT)&&(direction != LEFT)){
		direction=RIGHT;
	}
	PORTE->ISFR = BTN_UP | BTN_DOWN | BTN_LEFT | BTN_RIGHT;
}

/* Function moves snake position according to current direction */
void move(int direction){
	for(int i=SNAKE_LENGTH-1; i>=0; i--){
		if(i == 0){
			switch(direction){
				case DOWN:
					snake[i].y+=1;
					break;
				case UP:
					snake[i].y-=1;
					break;
				case LEFT:
					snake[i].x-=1;
					break;
				case RIGHT:
					snake[i].x+=1;
					break;
				default:
					break;
			}
			if(snake[i].y == 16){
				snake[i].y=0;
			}
			if(snake[i].y == -1){
				snake[i].y=15;
			}
			if(snake[i].x == -1){
				snake[i].x=7;
			}
			if(snake[i].x == 8){
				snake[i].x=0;
			}
		}
		else{
			snake[i].x=snake[i-1].x;
			snake[i].y=snake[i-1].y;
		}
	}
}

/* Function handles clock interruptions */
void PIT0_IRQHandler(void){
	PIT_TFLG0 |= PIT_TFLG_TIF_MASK;
	PIT_TCTRL0 = 0;
	for(int i=0; i<10; i++) {		//delay
		for(int j=0; j<10; j++){
			for(int k = 0; k < SNAKE_LENGTH; k++){
					PTA->PDOR &= GPIO_PDOR_PDO(CLEAR_ROWS);
					column_select(snake[k].y);
					row_select(snake[k].x);
					delay(10,35);	//more delay
			}
		}
	}

	move(direction);
	PIT_TCTRL0 |= PIT_TCTRL_TEN_MASK | PIT_TCTRL_TIE_MASK;

}

/* Initialize snake at the start */
void snake_init(){
	int x=0;
	int y=0;
	snake[0].x=x_start; //head of snake
	snake[0].y=y_start;
	for(int i=1; i<SNAKE_LENGTH; i++){
		if(x_start - i <0){
			x= x-i-8;
		}
		else{
			x=x-i;
		}
		snake[i].x=x;
		snake[i].y=y;
	}
}

int main(void)
{
	SystemConfig();
	PIT_init();
	snake_init();

    for (;;) {

    }
    /* Never leave main */
    return 0;
}
