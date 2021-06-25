using System.Collections.ObjectModel;
using System.Linq;
using ICSproject.BL.Models.DetailModels;

namespace UI_of_app.Wrappers
{
    public class InterpretWrapper : ModelWrapper<InterpretDetailModel>
    {
        public InterpretWrapper(InterpretDetailModel model)
            : base(model)
        {
            InitializeCollectionProperties(model);
        }

        public string Name
        {
            get => GetValue<string>();
            set => SetValue(value);
        }
        public string Genre
        {
            get => GetValue<string>();
            set => SetValue(value);
        }
        public string ImageSrc
        {
            get => GetValue<string>();
            set => SetValue(value);
        }
        public string Country
        {
            get => GetValue<string>();
            set => SetValue(value);
        }
        public string LongDescription
        {
            get => GetValue<string>();
            set => SetValue(value);
        }
        public string ShortDescription
        {
            get => GetValue<string>();
            set => SetValue(value);
        }



        private void InitializeCollectionProperties(InterpretDetailModel model)
        {
            if (model.Concerts == null)
            {
                return;

            }
            Concerts = new ObservableCollection<TimeSlotConcertWrapper>(
                model.Concerts.Select(e => new TimeSlotConcertWrapper(e)));

            RegisterCollection(Concerts, model.Concerts);
        }

        public ObservableCollection<TimeSlotConcertWrapper> Concerts { get; set; }

        



        public static implicit operator InterpretWrapper(InterpretDetailModel detailModel)
            => new(detailModel);

        public static implicit operator InterpretDetailModel(InterpretWrapper wrapper)
            => wrapper.Model;
    }
}