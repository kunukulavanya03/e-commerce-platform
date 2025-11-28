import React from 'react';
import styles from './HeroSection.module.css';

export default function HeroSection() {
  return (
    <section className={styles.hero}>
      <h1>Welcome to our E-commerce Platform</h1>
      <p>Discover the best products and deals</p>
      <button>Shop Now</button>
    </section>
  );
}
