using System.Collections.ObjectModel;
using System.Linq;
using ICSproject.BL.Models.DetailModels;

namespace UI_of_app.Wrappers
{
    public class StageWrapper : ModelWrapper<StageDetailModel>
    {
        public StageWrapper(StageDetailModel model)
            : base(model)
        {
            InitializeCollectionProperties(model);
        }


        public string Name
        {
            get => GetValue<string>();
            set => SetValue(value);
        }
        public string Description
        {
            get => GetValue<string>();
            set => SetValue(value);
        }
        public string ImgSrc
        {
            get => GetValue<string>();
            set => SetValue(value);
        }



        private void InitializeCollectionProperties(StageDetailModel model)
        {
            if (model.TimeSlots == null)
            {
                return;
            }
            TimeSlots = new ObservableCollection<TimeSlotConcertWrapper>(
                model.TimeSlots.Select(e => new TimeSlotConcertWrapper(e)));

            RegisterCollection(TimeSlots, model.TimeSlots);
        }

        public ObservableCollection<TimeSlotConcertWrapper> TimeSlots { get; set; }



        public static implicit operator StageWrapper(StageDetailModel detailModel)
            => new(detailModel);

        public static implicit operator StageDetailModel(StageWrapper wrapper)
            => wrapper.Model;
    }
}