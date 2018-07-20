Sample notebooks and data for Dotscience demos.

## To run:

1. Clone the repo

2. Clone [Dotscience](https://github.com/dotmesh-io/dotscience) repo and install according to its instructions. Start using `yarn`.

3. Clone the [experiment tracker](https://github.com/dotmesh-io/dotscience-ui-spike) repo. Inside that repo, run:
`docker-compose build`
`docker-compose up`
(note that you don't need to follow all the instructions on this repo's README.
You should see the experiment tracker running on localhost.

4. Each ipython notebook here is a self-contained demo, to be used in conjunction with the experiment tracker. 
Note that each requires the following 'input dots' to be set on the Dotscience local app:

`house_prices_tf`: set an output folder called 'model. No need for an input folder as the data is drawn from Google cloud storage.
`house_prices_py`: create two input dots for agent1 and agent 2, containing the respective CSVs. 
