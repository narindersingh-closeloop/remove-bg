Rails.application.routes.draw do
  devise_for :users
  root to: 'home#index'

  post '/edit_image' => 'home#edit_image', :as => :edit_image

  get '/show_image' => 'home#show_image', :as => :show_image

  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
end
