import { useState } from 'react';
import { Card, Button, Container, Row, Col, Badge } from 'react-bootstrap';

interface Scooter {
  Id: number;
  model: string;
  battery_capacity: number;
  battery_level: number;
  status: string;
  last_maintenance_date: string;
}

const Rental = () => {
  const [scooters, setScooters] = useState<Scooter[]>([
    {
      Id: 1,
      model: 'Xiaomi M365',
      battery_capacity: 99,
      battery_level: 45,
      status: 'availible',
      last_maintenance_date: '2025-03-19',
    },
    {
      Id: 6,
      model: 'Yandex pro',
      battery_capacity: 98,
      battery_level: 78,
      status: 'rented',
      last_maintenance_date: '2025-03-01',
    },
    {
      Id: 7,
      model: 'Ninebot mini',
      battery_capacity: 67,
      battery_level: 87,
      status: 'maintenance',
      last_maintenance_date: '2025-03-06',
    },
    {
      Id: 8,
      model: 'Sigway ultra',
      battery_capacity: 87,
      battery_level: 99,
      status: 'availible',
      last_maintenance_date: '2025-02-25',
    },
  ]);

  // Функция для выбора цвета бейджа статуса
  const getStatusVariant = (status: string) => {
    switch (status) {
      case 'availible':
        return 'success';
      case 'rented':
        return 'warning';
      case 'maintenance':
        return 'danger';
      default:
        return 'secondary';
    }
  };

  return (
    <Container>
      <h1 className="my-4 text-center">Аренда самокатов</h1>
      <Row>
        {scooters.map((scooter) => (
          <Col key={scooter.Id} md={6} lg={4} className="mb-4">
            <Card>
              <Card.Body>
                <Card.Title>{scooter.model}</Card.Title>
                <Badge bg={getStatusVariant(scooter.status)} className="mb-2">
                  {scooter.status.toUpperCase()}
                </Badge>
                <Card.Text>
                  <strong>Батарея:</strong> {scooter.battery_level}% (макс.{' '}
                  {scooter.battery_capacity}%
                  %) <br />
                  <strong>Последнее ТО:</strong>{' '}
                  {new Date(scooter.last_maintenance_date).toLocaleDateString()}
                </Card.Text>
                <Button
                  variant="primary"
                  disabled={scooter.status !== 'availible'}
                >
                  Арендовать
                </Button>
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>
    </Container>
  );
};

export default Rental;