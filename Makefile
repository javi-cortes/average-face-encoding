help:
	@echo "help                               -- prints this help"
	@echo "build                              -- builds Docker containers"
	@echo "run                                -- start the average face calculus"
	@echo "test                               -- start test suite"

GREEN="\\e[32m"
BLUE="\\e[94m"
REGULAR="\\e[39m"
RED="\\e[91m"

run:
	@echo "${BLUE}Downloading images...${REGULAR}"
	@docker run -v $(PWD)/image_crawler:/app/image_crawler/ average-face-calculus
	@echo "${BLUE}Finished${REGULAR}"
	@echo "${BLUE}Calculating average face encodings...${REGULAR}"
	@docker run -v $(PWD)/image_crawler:/app/image_crawler/ average-face-calculus python main.py
	@echo "${BLUE}Finished${REGULAR}"

build:
	docker build . -t average-face-calculus

test:
	docker run average-face-calculus python -m unittest discover

.PHONY: help build run test
