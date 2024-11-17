'use client';

import { useState } from 'react';

const eventsData = [
  { id: 1, title: 'Event 1', description: 'Details about Event 1' },
  { id: 2, title: 'Event 2', description: 'Details about Event 2' },
  { id: 3, title: 'Event 3', description: 'Details about Event 3' },
];

export default function EventsPage() {
  const [currentSlide, setCurrentSlide] = useState(0);

  const handleNext = () => {
    setCurrentSlide((prev) => (prev + 1) % eventsData.length);
  };

  const handlePrev = () => {
    setCurrentSlide(
      (prev) => (prev - 1 + eventsData.length) % eventsData.length
    );
  };

  return (
    <div
      style={{
        position: 'relative',
        height: '100vh',
        backgroundColor: '#f5f5f5',
        padding: '20px',
      }}
    >
      {/* Top-Right Heading */}
      <h1
        style={{
          position: 'absolute',
          top: '20px',
          right: '20px',
          fontSize: '24px',
          color: '#333',
        }}
      >
        Events
      </h1>

      {/* Carousel */}
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          alignItems: 'center',
          height: '100%',
        }}
      >
        <div
          style={{
            width: '80%',
            height: '300px',
            backgroundColor: '#fff',
            borderRadius: '12px',
            boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            padding: '20px',
            textAlign: 'center',
          }}
        >
          <div>
            <h2 style={{ fontSize: '20px', color: '#333' }}>
              {eventsData[currentSlide].title}
            </h2>
            <p style={{ color: '#666' }}>
              {eventsData[currentSlide].description}
            </p>
          </div>
        </div>

        {/* Navigation Buttons */}
        <div
          style={{
            marginTop: '20px',
            display: 'flex',
            justifyContent: 'center',
            gap: '10px',
          }}
        >
          <button
            onClick={handlePrev}
            style={{
              padding: '10px 20px',
              backgroundColor: '#007bff',
              color: '#fff',
              border: 'none',
              borderRadius: '5px',
              cursor: 'pointer',
            }}
          >
            Previous
          </button>
          <button
            onClick={handleNext}
            style={{
              padding: '10px 20px',
              backgroundColor: '#007bff',
              color: '#fff',
              border: 'none',
              borderRadius: '5px',
              cursor: 'pointer',
            }}
          >
            Next
          </button>
        </div>
      </div>
    </div>
  );
}
