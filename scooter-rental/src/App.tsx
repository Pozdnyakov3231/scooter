import { Routes, Route } from 'react-router-dom'; // Подключаем маршрутизацию
import Rental from './pages/Rental'; // Импортируем созданный нами компонент Rental

const App = () => (
  <Routes>
    <Route path="/" element={<Rental />} /> // Основной маршрут, открывающий страницу аренды
  </Routes>
);

export default App;