import axios from 'axios';

export const login = async (username, password) => {
  try {
    const response = await axios.post('/api/login', { username, password });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const register = async (username, email, password) => {
  try {
    const response = await axios.post('/api/register', { username, email, password });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const resetPassword = async (email) => {
  try {
    const response = await axios.post('/api/reset-password', { email });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
