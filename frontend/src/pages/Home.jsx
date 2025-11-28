import React from 'react';
import styles from './Home.module.css';
import HeroSection from '../components/HeroSection';
import Card from '../components/Card';

export default function Home() {
  return (
    <div>
      <HeroSection />
      <section className={styles.cards}>
        <Card />
        <Card />
        <Card />
      </section>
    </div>
  );
}
