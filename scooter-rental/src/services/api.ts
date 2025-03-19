import axios from 'axios';

const API_URL = 'https://nocodeapi.com/your_instance/scooter_rental';

export const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Получение списка самокатов
export const getScooters = async () => {
  const response = await api.get('/scooters');
  return response.data;
};
