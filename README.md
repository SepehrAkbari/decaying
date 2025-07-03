# Simulating the Nuclear Decay of Cesium-137

Imagine the Isar 2 nuclear power plant in Germany, which was shut down in 2023, and the potential environmental impact of its operations. One of the most concerning by-products of nuclear fission is Cesium-137, a radioactive isotope with a half-life of about 30 years. This project aims to simulate the decay of Cesium-137 over a century, providing insights into its long-term decay process.

The goal of this project is to explore two different methods of simulating this decay: first using the Euler method, and then using the 4th order Runge-Kutta method.

## Assumptions

To have a perfect simulation, we need exact specific values for the initial conditions and parameters, which are hard to find. However, we can make some reasonable assumptions based on the available data. We have outlined these assumptions [here](/assumptions/assumptions.md).

## Usage

To run this simulation, you can first clone this repository:

```bash
git clone https://github.com/SepehrAkbari/decaying.git
cd decaying
```

Then you can run each method separately:

```bash
cd src
python euler.py
python rk4.py
```

You can also run our error analysis script to compare the two methods:

```bash
python error_analysis.py
cd ../
```

There is also a Jupyter notebook available for interactive exploration of the results. You can find it in the [notebook](/notebook/decaying.ipynb) directory.

```bash
cd notebooks
jupyter decaying.ipynb
```

## Contributing

To contribute to this project, you can fork this repository and create pull requests. You can also open an issue if you find a bug or wish to make a suggestion.

## License

This project is licensed under the [GNU General Public License (GPL)](LICENSE).