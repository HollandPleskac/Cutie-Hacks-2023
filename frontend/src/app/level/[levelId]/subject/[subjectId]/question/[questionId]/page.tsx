'use client'

import useSWR from 'swr'
import { useRouter } from 'next/navigation'

export default function QuestionPage({ params }: any) {
    const router = useRouter()

    const { levelId, subjectId, questionId } = params;

    const fetcher = async (url: any) => {
        // console.log("fetching from url", url)
        const res = await fetch(url)
        if (!res.ok) {
            throw new Error(res.statusText);
        }
        // console.log("q/a pair result",resJSON ) // can only read res.json() once so make variable for it if need to log it here
        return res.json()
    }

    const apiUrl = levelId && subjectId && questionId ? `http://localhost:8000/${levelId}/${subjectId}/${questionId}` : null;

    const { data, error } = useSWR(apiUrl, fetcher);

    if (error) {
        console.log("see err",error)
        return (
            <div className='h-screen w-full bg-blue-400 flex justify-center items-center'>
                <p className='text-white text-lg'>Sorry, that question does not exist</p>
            </div>
        );
    }

    if (!data) return <div></div>;

    return (
        <div className='h-screen w-full bg-blue-400' >
            {"test"}
            <button onClick={() => {
                if (router)
                    router.push(`/level/${levelId}/subject/${subjectId}/question/${parseInt(questionId) + 1}`)
            }} >Next</button>
        </div>
    );
}
