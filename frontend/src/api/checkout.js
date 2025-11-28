import axios from 'axios';

export const checkout = async (paymentMethod, shippingAddress) => {
  try {
    const response = await axios.post('/api/checkout', { payment_method: paymentMethod, shipping_address: shippingAddress });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
