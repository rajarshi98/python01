text = "X-DSPAM-Confidence: 0.8475";

dot=text.find('.')

print float (text[dot:])
