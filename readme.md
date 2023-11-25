# **Stegger**
> Stegger can generate steganography content with message or script.

## **Prerequest**:
> python -m setup install --user

## **Usage**:
### message content restriction
> Last charactor of message or script must be ")"

### what to do with steganography content
> You can post steganography content on any social media plaforms and convert it back to message or script.

### convert message to steganography content
> This line will generate steganography content and save it to output.txt
#### for text file
> python main.py -e your-file.txt
#### for python file
> python main.py -e your-file.py

### convert steganography content to message
> This line will convert stegaongraphy content into message and save it to message.txt
> python main.py -d output.txt 

## **Todo**:
1. Using meaningful content like sentence or essay instead of random charactors
2. Encrypting steganography content for unpredictability
3. Convert last elements of steganography content to original characters without restriction that last charactor must be ")" and append sequence of "#" at the end of message or script

## **Disclaimer**
This code was created entirely out of an interest in learning about steganography. It should never be used for any malicious activities.
