# Use an official Node.js image
FROM node:20

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend files
COPY . .

# Expose the port Vite runs on
EXPOSE 3000

# Start the frontend
CMD ["npm", "run", "dev"]
