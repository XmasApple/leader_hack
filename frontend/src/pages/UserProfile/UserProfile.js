import s from './UserProfile.module.css';
import Container from '../../componnets/Col/Container/Container';
import user_profile_img_bg from '../../statics/user_profile_img_bg.png';
import UserCard from '../../componnets/UserCard/UserCard';

const UserProfile = () => {
    return (    
        <>
            <div className={s.user_profile_bg}>
                <img src={user_profile_img_bg} alt="" />
            </div>
            <section>
                <div className={s.user_profile}>
                    <Container>
                        <div>
                            <h3>Петров Алексей Павлович</h3>
                            <p className={s.user_profile_subTitle}>
                                Пользователь #123
                            </p>
                        </div>
                    </Container>
                    <UserCard />
                </div>
            </section>
        </>
    );
};

export default UserProfile;
