<a name="readme-top"></a>
<div align="center">
    <a href="https://github.com/liris-xr/PLUME">
        <picture>
            <source media="(prefers-color-scheme: dark)" srcset="https://github.com/liris-xr/PLUME-Protos/blob/fb65cf9da7104e3dfbe84a3688329ca2d5fbac52/Documentation~/Images/plume_banner_dark.png?raw=true">
            <source media="(prefers-color-scheme: light)" srcset="https://github.com/liris-xr/PLUME-Protos/blob/fb65cf9da7104e3dfbe84a3688329ca2d5fbac52/Documentation~/Images/plume_banner_light.png?raw=true">
            <img alt="PLUME banner." src="https://github.com/liris-xr/PLUME-Protos/blob/fb65cf9da7104e3dfbe84a3688329ca2d5fbac52/Documentation~/Images/plume_banner_light.png?raw=true">
        </picture>
    </a>
    <br />
    <br />
    <p align="center">
        <strong>PLUME: Record, Replay, Analyze and Share User Behavior in 6DoF XR Experiences</strong>
        <br />
        Charles Javerliat, Sophie Villenave, Pierre Raimbaud, Guillaume Lavoué
        <br />
        <em>(Journal Track) IEEE Conference on Virtual Reality and 3D User Interfaces</em>
        <br />
        <a href="https://www.youtube.com/watch?v=_6krSw7fNqg"><strong>Video »</strong><a>
        <a href="https://hal.science/hal-04488824"><strong>Paper »</strong></a>
        <a href="https://github.com/liris-xr/PLUME/wiki/"><strong>Explore the docs »</strong></a>
        <br />
        <br />
        <a href="https://github.com/liris-xr/PLUME/issues">Report Bug</a>
        ·
        <a href="https://github.com/liris-xr/PLUME/issues">Request Feature</a>
    </p>
</div>

<details>
    <summary>Table of Contents</summary>
    <ol>
        <li><a href="#about-plume-protos">About PLUME Protos</a></li>
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
        <li><a href="#citation">Citation</a></li>
    </ol>
</details>

## About PLUME Protos
This repository stores the definition for samples used by the <a href="https://github.com/liris-xr/PLUME-Recorder">PLUME Recorder</a>. These samples are based on <a href="https://github.com/protocolbuffers/protobuf">protobuf</a> to ease serialization on any platform.

## Getting Started

Start by cloning the repository using the following command:
```console
git clone https://github.com/liris-xr/PLUME-Protos.git
```

### How to build

Install the Buf CLI by following the steps [here](https://buf.build/docs/installation/).

```console
buf generate
```

A folder `generated/` will be created, containing all the generated classes for Python and C#.

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

Distributed under the <a rel="license" href="https://github.com/liris-xr/PLUME-Protos/blob/master/LICENSE">GPLv3 License</a>.

## Contact

Charles JAVERLIAT - charles.javerliat@gmail.com

Sophie VILLENAVE - sophie.villenave@ec-lyon.fr

## Citation
```
@article{javerliat_plume_2024,
	title = {{PLUME}: {Record}, {Replay}, {Analyze} and {Share} {User} {Behavior} in {6DoF} {XR} {Experiences}},
	url = {https://ieeexplore.ieee.org/document/10458415},
	doi = {10.1109/TVCG.2024.3372107},
	journal = {IEEE Transactions on Visualization and Computer Graphics},
	author = {Javerliat, Charles and Villenave, Sophie and Raimbaud, Pierre and Lavoué, Guillaume},
	year = {2024},
	note = {Conference Name: IEEE Transactions on Visualization and Computer Graphics},
	pages = {1--11}
}
```