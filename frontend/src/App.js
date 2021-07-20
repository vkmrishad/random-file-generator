import { Button, Card, Table, Container, Row, Col } from 'react-bootstrap';

import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <Container className="container-main">
      <Card>
        <Card.Header as="h5">Random File Generator</Card.Header>
        <Card.Body>
          <Button variant="primary">Generate</Button><br /><br />
          <Card.Text>Link:
            <Card.Link href="http://google.com" target="_blank">"http://google.com"</Card.Link>
          </Card.Text>
          <Button variant="warning">Report</Button><br /><br />
          <Row xs={2} md={2} lg={2}>
            <Col>
              <Table striped bordered hover>
                <thead>
                  <tr>
                    <th>Type</th>
                    <th>Count</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>1</td>
                    <td>Mark</td>
                  </tr>
                </tbody>
              </Table>
            </Col>
          </Row>
        </Card.Body>
      </Card>
    </Container>
  );
}

export default App;
