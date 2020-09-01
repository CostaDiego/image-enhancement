# Dev Folder

The Dev folder contains the development of the multiple algorithms related to this project. The structure of this folder are that in each subfolder contains a different algorithm.

## Folders

### CLAHE

The [CLAHE folder](./clahe) contains the OpenCV script to the technique known as Contrast Limited Adaptive Histogram Equalization (CLAHE). This script were implemented using python 3. This algorithm receives a image as parameter and enhances its quality.

The file in this folder is:

- [applyCLAHE.py](./clahe/applyCLAHE.py)

#### Usage

To use this script go into the [CLAHE folder](./clahe) and type in the terminal:

```bash
python3 applyCLAHE.py <path_to_image> [args]
```

The possible arguments are:
- `--save <path>` : The path to save the image. Optional.
- `--showImage [True | False]` : Switch if the image will showed or not. Optional. Defalt: `True`

### Socket

The [Socket Folder](./socket) contains the algorithm to communicate two different process. This script were implemented using python and one of its modules, the socket module. This algorithm sends message from the client to server and receives the response.

The files in this folder are:

- [client.py](./socket/client.py)
- [server.py](./socket/server.py)

#### Usage

To use this scripts go into the [Socket Folder](./socket) and open the server in a terminal, using the following command:

```bash
python3 server.py
```

After that, in another terminal, open the client, typing:

```bash
python3 client.py
```

Once this process are done, in the client terminal, just type the message and press enter.