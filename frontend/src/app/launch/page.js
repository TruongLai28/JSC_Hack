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

  return (
    <div className='relative z-20 flex flex-col items-center justify-center min-h-screen'>
      {/* Header */}
      <h1 className='absolute top-4 left-4 text-2xl font-bold text-white'>
        Launch Page
      </h1>

      {/* "What are you?" Section */}
      <div className='w-full max-w-md bg-gray-800 p-6 rounded-lg shadow-md mb-6'>
        <h2 className='text-lg font-semibold mb-4 text-white'>What are you?</h2>
        <div className='space-y-3 text-white'>
          {['Student', 'Teacher', 'Both'].map((option) => (
            <div key={option} className='flex items-center space-x-2'>
              <Checkbox id={option} className='bg-white border-gray-300' />
              <Label htmlFor={option}>{option}</Label>
            </div>
          ))}
        </div>
      </div>

      {/* "Field of Study" Section */}
      <div className='w-full max-w-md bg-gray-800 p-6 rounded-lg shadow-md mb-6'>
        <h2 className='text-lg font-semibold mb-4 text-white'>
          Field of Study
        </h2>
        <Select>
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
    </div>
  );
}
