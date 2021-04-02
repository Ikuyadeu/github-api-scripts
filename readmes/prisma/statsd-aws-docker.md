# Node StatsD docker image with AWS backend
Our docker image with preinstalled statsd (node) + AWS backend for statsd.

Uses our [fork of the AWS backend for statsd](https://github.com/graphcool/aws-cloudwatch-statsd-backend), which allows us to use ENV vars instead of baking AWS credentials and region into the image (+ it has better logging).

# Build & Use
- `cp config.js.example config.js`
- Build image with `make build-local` (dev) or `make build` (prod)
- `make push` to push the latest build to dockerhub
- Make sure the following env vars are present in the container:
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - AWS_REGION
- Then you can use the image `graphcool/graphcool-statsd-aws:latest`

## Local test setup
If you want to start the container locally and connect it to AWS, simply inject the env vars into the container, for example via a .dockerenv file that has key=value pairs: `docker run -it --env-file=.dockerenv -p 8125:<mapping> graphcool/graphcool-statsd-aws:latest`

If you just want a local statsd container without any AWS connection: `make build-local` and spin up that image. 

Note that network=host doesn't work on OSX! You need to map the port.

# Q & A
Q: Why the --no-cache on build?
A: Docker caches the npm install of the git repo. To fetch the latest we need to disable caching, unfortunately. The build is still fairly fast, though.