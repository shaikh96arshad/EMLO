import torch
import urllib
import argparse
from json import dumps
from PIL import Image
from torchvision import transforms
import logging

def main():
    # load pretrained pytorch model
    parser = argparse.ArgumentParser(description="example")
    parser.add_argument("--model",dest="model",help="model to use")
    parser.add_argument("--image",dest="image",help="Image of model")
    args = parser.parse_args()

    logging.disable(logging.CRITICAL)
    model = torch.hub.load('pytorch/vision:v0.10.0', args.model, pretrained=True,)
    model.eval()
    logging.disable(logging.CRITICAL)
    # load sample image & its url
    url, filename = (args.image, "temp.jpg")
    try: urllib.URLopener().retrieve(url, filename)
    except: urllib.request.urlretrieve(url, filename)

    input_image = Image.open(filename)
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])
    ])

    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)

    if torch.cuda.is_available():
        input_batch = input_batch.to('cuda')
        model.to('cuda')

    with torch.no_grad():
        output = model(input_batch)

    probablities = torch.nn.functional.softmax(output[0],dim=0)

    with open("Session2/imagenet_classes.txt") as f:
        categories = [s.strip() for s in f.readlines()]

    top1_prob_idx = torch.argmax(probablities).item()
    top1_prob = torch.max(probablities).item()
    top1_class = categories[top1_prob_idx]

    out = {"predicted" : top1_class, "confidence":top1_prob}
    print(dumps(out))

if __name__ == '__main__':
    logging.disable(logging.CRITICAL)
    main()