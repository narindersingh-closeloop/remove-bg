class HomeController < ApplicationController
  def index
  end

  def edit_image

    file_path = params[:uploaded_data_file][:location].path

    # execute python script
    @image = `python3 lib/assets/python/edit_image.py "#{file_path}"`

    redirect_to show_image_path(image: @image)
  end

  def show_image
    @image = params[:image].split("\n").last
  end
end
