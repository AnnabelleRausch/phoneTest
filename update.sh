#!/bin/bash
echo "AWS Lambda Update"
rm ZipFiles/upload.zip
zip -r ZipFiles/upload.zip lambda_function.py voice_response.json rnv_api.py alexa_response.py
aws lambda update-function-code --function-name arn:aws:lambda:eu-west-1:095485643790:function:MyPhoneNumber --zip-file fileb://ZipFiles/upload.zip --region eu-west-1
echo "Done!!"