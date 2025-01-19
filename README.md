# Ashian

Ashian is a platform designed to facilitate the adoption of animals in need of care and to help locate lost animals. It provides access to animal shelters, veterinary clinics, and pet food suppliers.

---

## Features
- Register and manage animal profiles for adoption.
- Report and search for lost animals.
- Connect with nearby shelters, veterinarians, and suppliers.
- Interactive map for easy navigation and location services.

---

## Prerequisites
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/paris-hh/Ashian.git
cd Ashian
```

### Environment Variables
Create a `.env` file in the root directory with the following content:
```env
POSTGRES_DB=ashian
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
DATABASE_URL=postgres://postgres:password@postgres:5432/ashian
```

### Start the Application
Use Docker Compose to build and run the application:
```bash
docker-compose up --build
```

The application will be accessible at `http://localhost:8000`.

---

## Usage
1. Open your browser and navigate to `http://localhost:8000`.
2. Explore features such as registering animals, reporting lost pets, and locating nearby services.

---

## Dependencies
Python package dependencies are listed in `requirements.txt` and installed automatically via Docker.

---

## Contributing
We welcome contributions to Ashian! To contribute:
1. Fork the repository.
2. Create a feature branch: `git checkout -b yourName/typeOfBranch/title`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin branch-name`.
5. Open a pull request.

---

## License
Ashian is licensed under the Beerware License. You are free to use the software as you wish. If you like it, buy the developer a beer in return. Cheers! 🍻
