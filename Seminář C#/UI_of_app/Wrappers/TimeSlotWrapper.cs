using System;
using ICSproject.BL.Models.DetailModels;
using ICSproject.BL.Models.ListModels;

namespace UI_of_app.Wrappers
{
    public class TimeSlotWrapper : ModelWrapper<TimeSlotDetailModel>
    {
        public TimeSlotWrapper(TimeSlotDetailModel model)
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
        public StageListModel Stage
        {
            get => GetValue<StageListModel>();
            set => SetValue(value);
        }
        public InterpretListModel Interpret
        {
            get => GetValue<InterpretListModel>();
            set => SetValue(value);
        }


        public static implicit operator TimeSlotWrapper(TimeSlotDetailModel detailModel)
            => new(detailModel);

        public static implicit operator TimeSlotDetailModel(TimeSlotWrapper wrapper)
            => wrapper.Model;
    }
}