import React from 'react';
import BusinessPlatformItem from "../BusinessPlatformItem/BusinessPlatformItem";
import Row from "../Col/Row/Row";
import Col from "../Col/Col/Col";
import Container from "../Col/Container/Container";

const BusinessPlatformList = () => {
    return (
        <section>
            <Container>
                <Row>
                    <Col colWidth={'col_3'}>
                        <BusinessPlatformItem>Cube.Moscow</BusinessPlatformItem>
                    </Col>
                </Row>
            </Container>
        </section>
    );
};

export default BusinessPlatformList;