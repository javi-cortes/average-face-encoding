<!-- ABOUT THE PROJECT -->
## About The Project
`average-face-encoding` Calculates the average face encoding of all the images
for a given website.

In this particular case, is a website that contains labeled faces for benchmark verification

<!-- GETTING STARTED -->
## Getting Started
***
You can use docker or Makefile to run the project.
### Prerequisites
In order to run the project you will need the following:
* [docker](https://docs.docker.com/engine/install/)
* [GNU Make](https://www.gnu.org/software/make/)

## How to
***
1. Rewrite .env.example to your own .env with the webpage you wanna obtain the
images from
2. Execute ```make {build,run}```
3. The average encoding result should be prompted and stored on average_face_encodings.txt


