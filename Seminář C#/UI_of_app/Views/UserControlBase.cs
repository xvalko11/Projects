using System.Windows;
using System.Windows.Controls;
using UI_of_app.ViewModels;

namespace UI_of_app.Views
{
    public abstract class UserControlBase : UserControl
    {
        protected UserControlBase()
        {
            Loaded += OnLoaded;
        }

        private void OnLoaded(object sender, RoutedEventArgs e)
        {
            if (DataContext is IListViewModel viewModel)
            {
                viewModel.Load();
            }
        }
    }
}
