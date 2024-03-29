import { useEffect, useState } from 'react'

export default function Time() {
  const [currentTime, setCurrentTime] = useState(0);
  useEffect(() => {
    const interval = setInterval(() => {
      fetch('http://localhost:5000/time', {
        method: 'GET',
        mode: 'cors'
      })
        .then(res => res.json())
        .then(data => {
          setCurrentTime(data.time);
        });
    }, 1000);
    return () => clearInterval(interval);
  }, []);
  return (
    <div className='time'>{currentTime}</div>
  )
}