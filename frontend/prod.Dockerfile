# Use the official Node.js 14 image as the base image
FROM node

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package.json .
COPY yarn.lock .

# Install dependencies using yarn (you can also use npm if you prefer)
RUN yarn

# Copy the entire project directory to the working directory
COPY . .

# Build the Vite React project
RUN yarn build

# Expose port 3000 (the default port used by Vite for development)
EXPOSE 80

# Command to start the application when the container starts
CMD ["yarn", "serve"]