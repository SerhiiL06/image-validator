<h2>Image Validation Service</h2>

This service validates images by their URLs. It accepts POST requests at /validate with the images_url key and returns URLs of valid images.

<h2>Setup:</h2>

1. Clone the repository:
```bash
git clone https://github.com/SerhiiL06/image-validator.git
```
2. Change work directory:
```bash
cd image-validator
```
3. Run docker-compose file:
```bash
docker-compose up
```

<h2>Usage:</h2>

1. Send a POST Request:
    - Send a POST request to http://localhost:8000/validate.
    - Include a JSON body with the key <b>images_url</b> containing URLs of the images you want to validate. Only URLs pointing to images with
       extensions jpg, jpeg, png, or webp are accepted.
   Example:
```json
 {
    "images_url": [
        "https://example.com/image1.jpg",
        "https://example.com/image2.png"
    ]
}
```
   
 
