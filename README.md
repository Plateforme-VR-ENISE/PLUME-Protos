<a name="readme-top"></a>
<div align="center">
    <h1>PLUME-Protos</h1>
</div>

<details>
    <summary>Table of Contents</summary>
    <ol>
        <li><a href="#about">About</a></li>
        <li>
            <a href="#getting-started">Getting Started</a>
            <ul>
                <li><a href="#prerequisites">Prerequisites</a></li>
                <li><a href="#how-to-build">How to build</a></li>
            </ul>
        </li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
        <li><a href="#contact">Contact</a></li>
    </ol>
</details>

## About

TODO

## Getting Started

Start by cloning the repository using the following command:
```console
git clone https://github.com/Plateforme-VR-ENISE/PLUME-Protos.git
```

### Prerequisites

Install `protoc` and put it in your PATH. You can find the procedure to install protoc [here](https://grpc.io/docs/protoc-installation/).
<br/>
Install `python` and put it in your PATH.

### How to build

#### Python

Simply run:
```console
python build_all_python.py
```
A folder `generated/python` will be created, containing all the `*_pb2.py` files.

#### C#

Simply run:
```console
python build_all_csharp.py
```
A folder `generated/csharp` will be created, containing all the `*.g.cs` files.

## Usage

Import the generated files in your project and use the messages with `protobuf`.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Licence Creative Commons
Attribution - Non Commercial 4.0 International</a>. See `LICENSE.md` for more information.

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a>

## Contact

Charles JAVERLIAT - charles.javerliat@gmail.com

Sophie VILLENAVE - sophie.villenave@enise.fr