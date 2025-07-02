## photos accessible @
### `https://henry-md.github.io/hosting/links/[img file]`
### `https://henry-md.github.io/hosting/links/vincent-dunn/podcasts/[audio file]`

ex. 
https://henry-md.github.io/hosting/links/personal/test_audio.m4a

Large files should be hosted on AWS: large files cannot be uploaded without git LFS (large file storage), but LFS will just make a pointer to the file publicly accessible, so it won't work in the url bar, or as the src in an audio file. So you have to host with a cloud provider and do other stuff:
- Create AWS bucket & upload
- Allow global reads in Permissions tab: 
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "PublicReadGetObject",
        "Effect": "Allow",
        "Principal": "*",
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*"
      }
    ]
  }
- Get public url from "Object URL" in default "properties" tab