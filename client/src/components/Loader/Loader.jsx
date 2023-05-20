import React from 'react';
import styles from './Loader.module.css';
import loading from './assets/loading.gif'

const Loader = () => {
    return (
        <div className={styles.loader}>
            <img src={loading} className={styles.loading }alt="loading"/>
        </div>
    )
}

export default Loader;