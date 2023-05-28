import React, {useState} from 'react';
import s from './AddingEmployee.module.css'
import BusinessSwiperShell from "../BusinessSwiperShell/BusinessSwiperShell";
import Row from "../Col/Row/Row";
import Col from "../Col/Col/Col";
import InputWithTitle from "../UI/InputWithTitle/InputWithTitle";
import TextInput from "../UI/TextInput/TextInput";
import UniversalButton from "../UI/UniversalButton/UniversalButton";

const AddingEmployee = () => {

    const [form, setForm] = useState({
        employee_id: '',
        employee_position: ''
    })

    const handleChange = (name, value) => {
        setForm({
            ...form,
            [name]: value,
        });
    };

    const onSubmit = () => {
        try {

        } catch (e) {

        }
    }

    return (
        <BusinessSwiperShell title={'Добавление нового сотрудника'}>
            <div className={s.block}>
                <Row>
                    <Col colWidth={'col_3'}>
                        <form onSubmit={onSubmit}>
                            <InputWithTitle name={'employee_id'} title={'ID сотрудника *'}>
                                <TextInput
                                    type={'text'}
                                    value={form.employee_id}
                                    onChange={(e) => handleChange('employee_id', e.target.value)}
                                    name={'employee_id'}
                                    placeholder={'Введите ID сотрудника'}
                                />
                            </InputWithTitle>
                            <InputWithTitle name={'employee_position'} title={'Должность сотрудника *'}>
                                <TextInput
                                    type={'text'}
                                    value={form.employee_position}
                                    onChange={(e) => handleChange('employee_position', e.target.value)}
                                    name={'employee_position'}
                                    placeholder={'Введите должность сотрудника'}
                                />
                            </InputWithTitle>
                            <p>* - обязательные поля для заполнения </p>
                            <UniversalButton
                                className={'fill_red'}
                                type={'submit'}
                                onClick={onSubmit}
                            >
                                Добавить
                            </UniversalButton>
                        </form>
                    </Col>
                </Row>
            </div>
        </BusinessSwiperShell>
    );
};

export default AddingEmployee;