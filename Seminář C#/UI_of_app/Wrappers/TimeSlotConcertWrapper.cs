using System;
using ICSproject.BL.Models.DetailModels;
using ICSproject.BL.Models.ListModels;

namespace UI_of_app.Wrappers
{
    public class TimeSlotConcertWrapper : ModelWrapper<TimeSlotConcert>
    {
        public TimeSlotConcertWrapper(TimeSlotConcert model)
            : base(model)
        {
        }

        public DateTime SlotStart
        {
            get => GetValue<DateTime>();
            set => SetValue(value);
        }
        public DateTime SlotEnd
        {
            get => GetValue<DateTime>();
            set => SetValue(value);
        }
        public String InterpretName
        {
            get => GetValue<String>();
            set => SetValue(value);
        }
        public String Stage
        {
            get => GetValue<String>();
            set => SetValue(value);
        }



        public static implicit operator TimeSlotConcertWrapper(TimeSlotConcert detailModel)
            => new(detailModel);

        public static implicit operator TimeSlotConcert(TimeSlotConcertWrapper wrapper)
            => wrapper.Model;
    }
}