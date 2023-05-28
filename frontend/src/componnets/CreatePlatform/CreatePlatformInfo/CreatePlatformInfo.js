import React from 'react';
import s from './CreatePlatformInfo.module.css'
import Row from "../../Col/Row/Row";
import Col from "../../Col/Col/Col";

const CreatePlatformInfo = ({children}) => {
    return (
        <div>
            {children.length > 1 ?
                <Row style={{justifyContent: 'space-between'}}>
                    <Col colWidth={'col_5'}>
                        {children[0]}
                    </Col>
                    <Col colWidth={'col_6'}>
                        {children[1]}
                    </Col>
                </Row>
                :
                children
            }
        </div>
    );
};

export default CreatePlatformInfo;