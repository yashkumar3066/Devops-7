# Use an official OpenJDK runtime as the base image
FROM openjdk:21-jdk-slim

# Set the working directory in the container
WORKDIR /app

# Copy the JAR file into the container
# Update `CourseCatalog.jar` with your actual JAR file name
COPY target/CourseCatalogue-0.0.1-SNAPSHOT.jar app.jar

# Expose the port that the Spring Boot application will run on
EXPOSE 9090

# Run the application
ENTRYPOINT ["java", "-jar", "app.jar"]