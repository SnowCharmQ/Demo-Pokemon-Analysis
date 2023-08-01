import { Routes, Route } from 'react-router-dom';
import Home from './Home';
import Analysis from './Analysis';

export default function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/analysis" element={<Analysis />} />
      </Routes>
    </div>
  );
}
