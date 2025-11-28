import axios from 'axios';

export const getCart = async () => {
  try {
    const response = await axios.get('/api/cart');
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const addProductToCart = async (productId, quantity) => {
  try {
    const response = await axios.post('/api/cart', { product_id: productId, quantity });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
