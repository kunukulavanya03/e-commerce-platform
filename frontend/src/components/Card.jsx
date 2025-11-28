import React from 'react';
import styles from './Card.module.css';

export default function Card() {
  return (
    <div className={styles.card}>
      <h2>Product Title</h2>
      <p>Product Description</p>
      <button>Buy Now</button>
    </div>
  );
}
