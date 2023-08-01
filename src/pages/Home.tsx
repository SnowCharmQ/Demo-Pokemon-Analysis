import pokemon from '../svg/pokemon.svg';
import '../styles/Home.css';
import { useNavigate } from 'react-router-dom';

export default function Home() {
    const navigate = useNavigate();
    const toAnalysis = () => {
        navigate('/analysis');
    };
    return (
        <div className="App">
            <header className="App-header">
                <img src={pokemon} className="App-logo" alt="logo" />
                <p>
                    Click on the text below to see the pokemon analysis results.
                </p>
                <div className='App-link' onClick={toAnalysis}>
                    Pokemon Analysis
                </div>
            </header>
        </div>
    );
}
