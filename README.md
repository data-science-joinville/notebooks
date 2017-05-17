# docker-notebooks

Docker container with Anaconda and some scientific Python stuff.

## Usage

You can download and run this image using the following commands:

```sh
docker pull magrathealabs/notebooks
```

And start the Jupyter Notebook server:

```sh
docker run --rm -it -p 8888:8888 -v "$(pwd):/notebooks" magrathealabs/notebooks
```

You can then view the Jupyter Notebook by opening `http://localhost:8888` in your browser.
