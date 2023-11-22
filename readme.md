# **Stegger**
> Stegger can convert message to steg and convert steg to message

## **Prerequest**:
> python -m setup install --user

## **Usage**:
### message content restriction
> Last charactor of message or script must be ")"

### convert message to steg
> This line will generate steganography content and save it to output.txt
> python main.py -e filepath

### convert steg to message
> This line will convert stegaongraphy content into message and save it to message.txt
> python main.py -d filepath

## **Todo**:
1. Using meaningful content like sentence or essay instead of random charactors
2. Encrypting steganography content for unpredictable steganography
3. Convert last elements of steg to original characters without restriction that last charactor must be ")"
