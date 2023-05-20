import { useState } from "react";
import { requestPromptResponse } from "../../services/api";
import styles from "./Home.module.css";
import Loader from "../Loader/Loader";

export const Home = () => {
  const [message, setMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  
  const handleRequest = async () => {
    setIsLoading(true);
    const res = await requestPromptResponse();
    setMessage(res.message);
    setIsLoading(false);
  };
  
  return (
    <div className={styles.page}>
      <h3 className={styles.title}>Integration of Slack and Open AI</h3>
      <button className={styles.button} onClick={handleRequest}>
        Request
      </button>
      <div className={styles.messageContainer}>
        {message ?? <p className={styles.message}>{message}</p>}
      </div>
      {isLoading ? <Loader /> : <></>}
    </div>
  );
};
