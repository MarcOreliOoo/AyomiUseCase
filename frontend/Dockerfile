# Specify the base image
FROM node:20-alpine

# Set the working directory
WORKDIR /code/frontend

# Copy package.json
COPY ./package.json /package.json

# Install dependencies
RUN yarn install

# Copy the rest of the application code
COPY . /code/frontend

# Build the React app
# RUN yarn build

EXPOSE 3000

# Set the command to start the app
CMD ["yarn", "dev"]
