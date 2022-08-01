import os
import sys
import cv2
import torch

os.environ["CUDA_VISIBLE_DEVICES"]="-1"

def get_model():
    # loading best model weights
    best_weights = os.path.join('model_files', 'weights', 'best.pt')
    return torch.hub.load('ultralytics/yolov5', 'custom', best_weights)


def blur(model, image_path):
    # Read Image
    image = cv2.imread(image_path)
    # Predicting from model
    results = model(image)
    # df of results
    results_df= results.pandas().xyxy[0]
    # kernel size for blur
    ksize = (100, 100)
    # looping thorugh all number plates de3tected
    for ind, row in results_df.iterrows():
        y_min, y_max, x_min, x_max = int(row['ymin']), int(row['ymax']), int(row['xmin']), int(row['xmax'])
        image[y_min:y_max,x_min:x_max] = cv2.blur(image[y_min:y_max,x_min:x_max], ksize, cv2.BORDER_DEFAULT)

    # saving image
    cv2.imwrite(os.path.join('result_images', os.path.split(image_path)[1].split('.')[0]+'.png'), image)

def main():
    image_path = sys.argv[1]
    model = get_model()
    blur(model, image_path)

if __name__=='__main__':
    main()