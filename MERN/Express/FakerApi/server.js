const express = require('express');
const { faker } = require('@faker-js/faker');

const app = express();
const port = 8000;

app.use(express.json());

const createUser = () => {
  return {
    password: faker.internet.password(),
    email: faker.internet.email(),
    phoneNumber: faker.phone.number(),
    lastName: faker.person.lastName(),
    firstName: faker.person.firstName(),
    _id: faker.string.uuid(),

  };
};

const createCompany = () => {
  return {
    _id: faker.string.uuid(),
    name: faker.company.name(),
    address: {
      street: faker.location.streetAddress(),
      city: faker.location.city(),
      state: faker.location.state(),
      zipCode: faker.location.zipCode(),
      country: faker.location.country()
    }
  };
};

app.get('/api/users/new', (req, res) => {
  const newUser = createUser();
  res.json(newUser);
});

app.get('/api/companies/new', (req, res) => {
  const newCompany = createCompany();
  res.json(newCompany);
});

app.get('/api/user/company', (req, res) => {
  const newUser = createUser();
  const newCompany = createCompany();
  res.json({ user: newUser, company: newCompany });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});