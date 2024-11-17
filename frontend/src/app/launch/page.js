'use client';

import React, { useState } from 'react';
import { Checkbox } from '@/components/ui/checkbox';
import { Label } from '@/components/ui/label';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { Input } from '@/components/ui/input';
import { Badge } from '@/components/ui/badge';

export default function LaunchPage() {
  const [selectedInterests, setSelectedInterests] = useState([]);
<<<<<<< HEAD
  const [role, setRole] = useState('');
  const [fieldOfStudy, setFieldOfStudy] = useState('');
  const [results, setResults] = useState({
    ostem: null,
    pathway: null,
    event: null,
    research: null
  });
=======
>>>>>>> parent of 2b35164 (extra changes)
  const allInterests = [
    'Technology',
    'Science',
    'Math',
    'Art',
    'Music',
    'Sports',
  ];

  const toggleInterest = (interest) => {
    setSelectedInterests((prev) =>
      prev.includes(interest)
        ? prev.filter((item) => item !== interest)
        : [...prev, interest]
    );
  };

<<<<<<< HEAD
  const handleSubmit = async () => {
    const query = `I'm ${role}, my field of study is ${fieldOfStudy} and my interests are ${selectedInterests.join(', ')}`;
    
    const requestBody = { 
      query: query,
      num_results: 3
    };

    try {
      const endpoints = ['ostem', 'pathway', 'event', 'research'];
      const promises = endpoints.map(endpoint => 
        fetch(`http://localhost:8000/search/${endpoint}`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(requestBody)
        }).then(res => res.json())
      );

      const [ostemData, pathwayData, eventData, researchData] = await Promise.all(promises);
      
      // Save all results to state
      setResults({
        ostem: ostemData,
        pathway: pathwayData,
        event: eventData,
        research: researchData
      });

      // Log all responses
      console.log('OSTEM Response:', ostemData);
      console.log('Pathway Response:', pathwayData);
      console.log('Event Response:', eventData);
      console.log('Research Response:', researchData);

      // Save results to localStorage
      localStorage.setItem('searchResults', JSON.stringify({
        pathway: pathwayData,
        event: eventData,
        research: researchData
      }));

    } catch (error) {
      console.error('Error submitting form:', error);
    }
  };

=======
>>>>>>> parent of 2b35164 (extra changes)
  return (
    <div className='relative z-20 flex flex-col items-center justify-center min-h-screen'>
      {/* Header */}
      <h1 className='absolute top-4 left-4 text-2xl font-bold text-white'>
        Launch Page
      </h1>

<<<<<<< HEAD
      {/* "What are you?" Section - Updated with onChange */}
=======
      {/* "What are you?" Section */}
>>>>>>> parent of 2b35164 (extra changes)
      <div className='w-full max-w-md bg-gray-800 p-6 rounded-lg shadow-md mb-6'>
        <h2 className='text-lg font-semibold mb-4 text-white'>What are you?</h2>
        <div className='space-y-3 text-white'>
          {['Student', 'Teacher', 'Both'].map((option) => (
            <div key={option} className='flex items-center space-x-2'>
<<<<<<< HEAD
              <Checkbox 
                id={option} 
                className='bg-white border-gray-300'
                checked={role === option}
                onCheckedChange={() => setRole(option)}
              />
=======
              <Checkbox id={option} className='bg-white border-gray-300' />
>>>>>>> parent of 2b35164 (extra changes)
              <Label htmlFor={option}>{option}</Label>
            </div>
          ))}
        </div>
      </div>

<<<<<<< HEAD
      {/* "Field of Study" Section - Updated with onChange */}
      <div className='w-full max-w-md bg-gray-800 p-6 rounded-lg shadow-md mb-6'>
        <h2 className='text-lg font-semibold mb-4 text-white'>Field of Study</h2>
        <Select onValueChange={setFieldOfStudy} value={fieldOfStudy}>
=======
      {/* "Field of Study" Section */}
      <div className='w-full max-w-md bg-gray-800 p-6 rounded-lg shadow-md mb-6'>
        <h2 className='text-lg font-semibold mb-4 text-white'>
          Field of Study
        </h2>
        <Select>
>>>>>>> parent of 2b35164 (extra changes)
          <SelectTrigger className='w-full'>
            <SelectValue placeholder='Select a field of study' />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value='computer_science'>Computer Science</SelectItem>
            <SelectItem value='engineering'>Engineering</SelectItem>
            <SelectItem value='biology'>Biology</SelectItem>
            <SelectItem value='art'>Art</SelectItem>
            <SelectItem value='music'>Music</SelectItem>
            <SelectItem value='mathematics'>Mathematics</SelectItem>
          </SelectContent>
        </Select>
      </div>

      {/* "Interests" Section */}
      <div className='w-full max-w-md bg-gray-800 p-6 rounded-lg shadow-md'>
        <h2 className='text-lg font-semibold mb-4 text-white'>Interests</h2>
        <Input
          placeholder='Search interests...'
          className='mb-4'
          onChange={(e) => {
            // Handle filtering logic here, if necessary
          }}
        />
        <div className='flex flex-wrap gap-2'>
          {allInterests.map((interest) => (
            <Badge
              key={interest}
              onClick={() => toggleInterest(interest)}
              className={`cursor-pointer text-black ${
                selectedInterests.includes(interest)
                  ? 'bg-blue-500 text-white'
                  : 'bg-gray-200'
              }`}
            >
              {interest}
            </Badge>
          ))}
        </div>
      </div>
<<<<<<< HEAD

      {/* Submit Button - Updated with onClick */}
      <button 
        onClick={handleSubmit}
        className='mt-6 px-8 py-3 bg-gray-800 hover:bg-gray-700 text-white rounded-lg font-semibold transition-colors'
      >
        Submit
      </button>
=======
>>>>>>> parent of 2b35164 (extra changes)
    </div>
  );
}
